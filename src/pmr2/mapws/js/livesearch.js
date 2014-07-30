$(document).ready(function () {

    hookOwlInput(
        "#form-widgets-ontological_term",
        window.location.href.toString().replace(
            /map_query.*/, 'pmr2_ricordo/owlterms/'),
        updateMapClientTermSelection
    );

});

function updateMapClientTermSelection(item, value) {
    selectedTerm = item.replace(/[^(]*\((.*)\)/, '$1');
    div = $("#mapclient-term-details");
    if (div.length == 0) {
        // create the element
        console.log('create');
        $("#form-widgets-ontological_term").parent().append(
            '<span id="mapclient-term-details"></span>');
        div = $("#mapclient-term-details");
    }
    div.text(item);
    console.log(div);
    return selectedTerm;
}
