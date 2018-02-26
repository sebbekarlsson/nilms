document.addEventListener('DOMContentLoaded', function(e) {
    if (window.visitor) return;
    
    window.saveButton = document.getElementById('admin-save');
    
    saveButton.addEventListener('click', function(e) {
        popupManager.togglePopup('popup-loading');

        query = {};

        for (var i = 0; i < fields.length; i++) {
            var field = fields[i];
            query[field.getAttribute('id')] = field.innerText;
        }

        wpost(
            '/api/page/update/' + page_id,
            query,
            function(data) {
                setTimeout(function(){
                    popupManager.togglePopup('popup-loading');
                }, 500);
            }
        );
    });
});
