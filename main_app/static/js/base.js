document.addEventListener('DOMContentLoaded', function() {
    const typeSelect = document.getElementById('question_type_select');
    const choicesContainer = document.getElementById('choices-container');

    function updateForm() {
        const value = typeSelect.value;

        if (value === 'MC' || value === 'MA') {
            choicesContainer.style.display = 'block';
        } else {
            choicesContainer.style.display = 'none';
        }
    }

    typeSelect.addEventListener('change', updateForm);
    updateForm();
});
