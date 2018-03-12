window.loadFields = function() {
    wget('/api/page/data/' + page_id, function(data) {
        data = JSON.parse(data);

        for (var property in data) {
            if (data.hasOwnProperty(property)) {
                var field = document.getElementById(property);
                
                if (!field) continue;

                field.innerText = data[property];
                field.classList.remove('medium-editor-placeholder');
            }
        }
    });
};
