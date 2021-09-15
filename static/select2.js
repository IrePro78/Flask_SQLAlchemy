

$(document).ready(function () {

  $("select[id^='selA']").each(function() {
        console.log(this);
    $(this).select2({
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

  $("select[id^='selP']").each(function() {
        console.log(this);
    $(this).select2({
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
});

