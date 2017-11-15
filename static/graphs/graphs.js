window.onload = function() {

    window.line1 = new Morris.Line({
        // ID of the element in which to draw the chart.
        element: 'graph-1',
        // Chart data records -- each entry in this array corresponds to a point on
        // the chart.
        data: [
        ],
        // The name of the data record attribute that contains x-values.
        xkey: 'date',
        // A list of names of data record attributes that contain y-values.
        ykeys: ['price'],
        // Labels for the ykeys -- will be displayed when you hover over the
        // chart.
        labels: ['Price']
      });

    window.line2 = new Morris.Line({
        // ID of the element in which to draw the chart.
        element: 'graph-2',
        // Chart data records -- each entry in this array corresponds to a point on
        // the chart.
        data: [
          { year: '2008', value: 10 },
          { year: '2009', value: 30 },
          { year: '2010', value: 52 },
          { year: '2011', value: 12 },
          { year: '2012', value: 20 }
        ],
        // The name of the data record attribute that contains x-values.
        xkey: 'year',
        // A list of names of data record attributes that contain y-values.
        ykeys: ['value'],
        // Labels for the ykeys -- will be displayed when you hover over the
        // chart.
        labels: ['Value']
      });

    fetch('miiloos/comed/?limit=50')
    .then(
      function(response) {
        if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
            response.status);
          return;
        }

        // Examine the text in the response
        response.json().then(function(data) {
    	    line1.setData(data.results)          
        });
      }
    )
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    })
}
function msToTime(s) {
  var ms = s % 1000;
  s = (s - ms) / 1000;
  var secs = s % 60;
  s = (s - secs) / 60;
  var mins = s % 60;
  var hrs = (s - mins) / 60;

  return hrs + ':' + mins + ':' + secs + '.' + ms;
}
