
$(document).ready(function () {
    $('#selAuthor').select2({
        language: "pl",
        tags: true,
        ajax: {
            url: '/authors',
            type: 'post',
            dataType: 'json',
            delay: 250,
            processResults: function (data) {
                return {
                    results: $.map(data, function (item) {
                        return {id: item.id, text: item.name};
                    })
                };
            }
        },
        minimumInputLength: 2
    });
});





$(document).ready(function () {
    $('#selPublisher').select2({
        language: "pl",
        tags: true,
        ajax: {
            url: '/publishers',
            type: 'post',
            dataType: 'json',
            delay: 250,
            processResults: function (data) {
                return {
                    results: $.map(data, function (item) {
                        return {id: item.id, text: item.name};
                    })
                };
            }
        },
        minimumInputLength: 2
    });
});



$(document).ready(function () {

  $("select[id^='sel']").each(function(index, element) {

    $(element).select2({
        language: "pl",
        tags: true,
        ajax: {
            url: '/authors',
            type: 'post',
            dataType: 'json',
            delay: 250,
            processResults: function (data) {
                return {
                    results: $.map(data, function (item) {
                        return {id: item.id, text: item.name};
                    })
                };
            }
        },
        minimumInputLength: 2
    });
});
});


$(document).ready(function () {
    $('#selPublisher1').select2({

        language: "pl",
        tags: true,
        ajax: {
            url: '/publishers',
            type: 'post',
            dataType: 'json',
            delay: 250,
            processResults: function (data) {
                console.log(data);
                return {
                    results: $.map(data, function (item) {
                        return {id: item.id, text: item.name};
                    })
                };
            }
        },
        minimumInputLength: 2
    });
});
