//Add books select2 scripts


$(function () {

    $("#selAuthor").select2({
        language: "pl",
        tags: true,
        ajax: {
            url: '/authors',
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


$(function () {

    $("#selPublisher").select2({
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



//Edit books authors and publishers select2 scripts
$(function () {

        $('button').on('click', function(){
            var modalID = $('#modaledit'+$(this).attr('id'));
            $(modalID).find('#selAuthor1').select2({
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


$(function () {

        $('button').on('click', function(){
            var modalID = $('#modaledit'+$(this).attr('id'));
            $(modalID).find('#selPublisher1').select2({
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
    });




    var cover_list = [{
        id: "twarda", text: "twarda"},
    {
        id: "miękka", text: "miękka"}
    ];


//Add book cover_type select2 scripts

$(function () {

    $('button').on('click', function () {
        $("#addmodal").find('#selCover').select2({
            data: cover_list
        });
    });
});

//Edit books cover_type select2 scripts

$(function () {

    $('button').on('click', function(){
        var modalID = $('#modaledit'+$(this).attr('id'));
        $(modalID).find('#selCover1').select2({
            data:cover_list
        });
    });
});






