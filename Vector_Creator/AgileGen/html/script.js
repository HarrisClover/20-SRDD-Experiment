
document.getElementById('new-project-btn').addEventListener('click', function() {
    document.getElementById('main-dashboard').classList.add('hidden');
    document.getElementById('canvas-page').classList.remove('hidden');
    createNewCanvas();
});

function createNewCanvas() {
    const canvas = document.getElementById('drawing-canvas');
    canvas.width = 800;
    canvas.height = 600;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    // Additional setup for drawing tools can go here
}

document.getElementById('color-picker').addEventListener('input', function() {
    const color = this.value;
    // Apply the selected color to the drawing tool
});

document.getElementById('stroke-width').addEventListener('input', function() {
    const strokeWidth = this.value;
    // Apply the selected stroke width to the drawing tool
});

document.getElementById('add-layer').addEventListener('click', function() {
    const layerList = document.getElementById('layer-list');
    const newLayer = document.createElement('li');
    newLayer.textContent = `Layer ${layerList.children.length + 1}`;
    layerList.appendChild(newLayer);
});

document.getElementById('delete-layer').addEventListener('click', function() {
    const layerList = document.getElementById('layer-list');
    if (layerList.children.length > 0) {
        layerList.removeChild(layerList.lastChild);
    }
});

document.getElementById('move-layer-up').addEventListener('click', function() {
    const layerList = document.getElementById('layer-list');
    const selectedLayer = layerList.querySelector('.selected');
    if (selectedLayer && selectedLayer.previousElementSibling) {
        layerList.insertBefore(selectedLayer, selectedLayer.previousElementSibling);
    }
});

document.getElementById('move-layer-down').addEventListener('click', function() {
    const layerList = document.getElementById('layer-list');
    const selectedLayer = layerList.querySelector('.selected');
    if (selectedLayer && selectedLayer.nextElementSibling) {
        layerList.insertBefore(selectedLayer.nextElementSibling, selectedLayer);
    }
});

// Additional event listeners and functions for drawing tools and properties panel can be added here
