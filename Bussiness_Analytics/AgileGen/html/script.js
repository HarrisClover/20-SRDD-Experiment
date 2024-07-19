
document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('salesGraph').getContext('2d');
    const salesGraph = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            datasets: [{
                label: 'Sales',
                data: [1200, 1900, 3000, 5000],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    document.getElementById('visualizationType').addEventListener('change', function() {
        const type = this.value;
        salesGraph.config.type = type;
        salesGraph.update();
    });

    document.getElementById('saveVisualization').addEventListener('click', function() {
        alert('Visualization saved!');
    });

    document.getElementById('generateReport').addEventListener('click', function() {
        const loadingIndicator = document.getElementById('loadingIndicator');
        loadingIndicator.style.display = 'block';
        setTimeout(() => {
            loadingIndicator.style.display = 'none';
            const downloadReport = document.getElementById('downloadReport');
            downloadReport.style.display = 'block';
            downloadReport.href = '#';
            downloadReport.download = 'Sales_Report.pdf';
        }, 2000);
    });

    document.getElementById('saveCustomVisualization').addEventListener('click', function() {
        alert('Custom visualization saved!');
    });

    // Simulating data update for summary section
    document.getElementById('totalSales').innerText = '$11000';
    document.getElementById('averageSales').innerText = '$366.67';
});
