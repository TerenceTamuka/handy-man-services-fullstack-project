$(document).ready(function() {
    // Initialize Summernote
    $('#summernote').summernote({
        height: 480, // Set height
        callbacks: {
            onChange: function(contents, $editable) {
                // Update the hidden textarea with the editor's content
                $('#id_additional_info').val(contents);
            }
        }
    });
});