/**
 * Used to send a GET request.
 *
 * @param String url
 * @param function callback(response)
 */
var wget = function (url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            callback(xhr.responseText);
        }
    }
    xhr.open('GET', url, true);
    xhr.send(null);  
}

/**
 * Used to send a POST request.
 *
 * @param String url
 * @param Object data
 * @param function callback(response)
 */
var wpost = function (url, data, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            callback(xhr.responseText);
        }
    }
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(data));  
};


document.addEventListener('DOMContentLoaded', function(e) {
    window.editor = new MediumEditor('.editable');
    window.saveButton = document.getElementById('admin-save');
    window.page_id = document.querySelector('input[name="page_id"]').value;
    window.fields = document.querySelectorAll('.editable');

    wget('/api/page/data/' + page_id, function(data) {
        data = JSON.parse(data);

        for (var property in data) {
            if (data.hasOwnProperty(property)) {
                var field = document.getElementById(property);
                field.innerText = data[property];
            }
        }
    });

    saveButton.addEventListener('click', function(e) {
        query = {};

        for (var i = 0; i < fields.length; i++) {
            var field = fields[i];
            query[field.getAttribute('id')] = field.innerText;
        }

        wpost(
            '/api/page/update/' + page_id,
            query,
            function(data) {
                console.log(data);
            }
        );
    });
});
