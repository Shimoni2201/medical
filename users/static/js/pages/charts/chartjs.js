$(function () {
    new Chart(document.getElementById("line_chart").getContext("2d"), getChartJs('line'));
    new Chart(document.getElementById("bar_chart").getContext("2d"), getChartJs('bar'));
    new Chart(document.getElementById("radar_chart").getContext("2d"), getChartJs('radar'));
    new Chart(document.getElementById("pie_chart").getContext("2d"), getChartJs('pie'));
});

function getChartJs(type) {
    var config = null;
        fetch("http://127.0.0.1:8000/total_sales_by_month/")
      .then(response => response.json())
      .then(data => {
          console.log(data);

 config = {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: "purchase",
                    data: data.value,
                    backgroundColor: 'rgba(0, 188, 212, 0.8)'
                }, {
                        label: "sales",
                        data:data.value,
                        backgroundColor: 'rgba(233, 30, 99, 0.8)'
                    }]
            },
            options: {
                responsive: true,
                legend: false
            }
        }

      } )
    if (type === 'line') {
        config = {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: "purchase",
                    data: data.value,
                    borderColor: 'rgba(0, 188, 212, 0.75)',
                    backgroundColor: 'rgba(0, 188, 212, 0.3)',
                    pointBorderColor: 'rgba(0, 188, 212, 0)',
                    pointBackgroundColor: 'rgba(0, 188, 212, 0.9)',
                    pointBorderWidth: 1
                }, {
                        label: "sales",
                        data: data.value,
                        borderColor: 'rgba(233, 30, 99, 0.75)',
                        backgroundColor: 'rgba(233, 30, 99, 0.3)',
                        pointBorderColor: 'rgba(233, 30, 99, 0)',
                        pointBackgroundColor: 'rgba(233, 30, 99, 0.9)',
                        pointBorderWidth: 1
                    }]
            },
            options: {
                responsive: true,
                legend: false
            }
        }
    }
    else if (type === 'bar') {
         fetch("http://127.0.0.1:8000/total_sales_by_month/")
      .then(response => response.json())
      .then(data => {
          console.log(data);

 config = {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: "purchase",
                    data: data.value,
                    backgroundColor: 'rgba(0, 188, 212, 0.8)'
                }, {
                        label: "sales",
                        data:data.value,
                        backgroundColor: 'rgba(233, 30, 99, 0.8)'
                    }]
            },
            options: {
                responsive: true,
                legend: false
            }
        }

      } )

    }

    return config;
}