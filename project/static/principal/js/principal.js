document.addEventListener('DOMContentLoaded', function() {
    updateFormFields(); // Call the function on page load
});
function updateFormFields() {
    var permission = document.getElementById('permission').value;
    var additionalFields = document.getElementById('additional-fields');
    additionalFields.innerHTML = '';

    if (permission == '2') { // Professor
      additionalFields.innerHTML += `
        <div class="form-group">
            <label for="nome">Nome</label>
            <input type="text" class="form-control" id="nome" name="nome" required placeholder="Nome">
        </div>
        <div class="form-group">
            <label for="departamento">Departamento</label>
            <input type="text" class="form-control" id="departmento" name="departmento" required placeholder="Departamento">
        </div>

        <div class="form-group">
          <label for="codigo_professor">Código Professor</label>
          <input type="text" class="form-control" id="codigo_professor" name="codigo_professor" required placeholder="Código Professor">
        </div>`;
    }
  }