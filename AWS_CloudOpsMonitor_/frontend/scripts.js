async function fetchMetrics() {
    const response = await fetch('/metrics');
    const data = await response.json();
    const container = document.getElementById('metrics');
    container.innerHTML = JSON.stringify(data, null, 2);
}

fetchMetrics();
