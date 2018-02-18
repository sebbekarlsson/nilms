window.addEventListener('DOMContentLoaded', function(e) {
    if (!window.visitor)
        window.editor = new MediumEditor('.editable');
    
    window.page_id = document.querySelector('input[name="page_id"]').value;
    window.fields = document.querySelectorAll('.editable');
    
    // load all fields the first thing we do
    loadFields();
});
