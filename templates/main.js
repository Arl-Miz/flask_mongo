function toggleEditMode(id) {
    const inputField = document.querySelector(`[name="content"][data-id="${id}"]`);
    const editButton = document.querySelector(`button[data-id="${id}"]`);

    if (inputField) {
        inputField.parentNode.removeChild(inputField);
        editButton.textContent = "Edit";
        editButton.setAttribute("onclick", `toggleEditMode("${id}")`);
    } else {
        const spanElement = document.querySelector(`span[data-id="${id}"]`);
        const content = spanElement.textContent;
        const formElement = document.querySelector(`form[data-id="${id}"]`);
        const inputElement = document.createElement("input");
        inputElement.setAttribute("type", "text");
        inputElement.setAttribute("name", "name");
        inputElement.setAttribute("value", name);
        inputElement.setAttribute("data-id", id);
        spanElement.parentNode.insertBefore(inputElement, spanElement.nextSibling);
        editButton.textContent = "Cancel";
        editButton.setAttribute("onclick", "");
    }
}
