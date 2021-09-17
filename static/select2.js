
$(function () {

        $("button").on('click', function(){
            var modalID = $('#'+$(this).attr('id'));
            console.log(modalID)

        $(modalID).on('show.bs.modal', function (e) {
            console.log(e)
            let btn_id = $(e.relatedTarget).data('id')
            console.log(btn_id)

            $('modaledit'+ btn_id).find('#selAuthor1').select2({
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
});

//
//
// $(document).ready(function () {
//
//   $("select[id^='selP']").each(function() {
//         console.log(this);
//     $("#selPublisher1").select2({
//         language: "pl",
//         tags: true,
//         ajax: {
//             url: '/publishers',
//             type: 'post',
//             dataType: 'json',
//             delay: 250,
//             processResults: function (data) {
//                 console.log(data);
//                 return {
//                     results: $.map(data, function (item) {
//                         return {id: item.id, text: item.name};
//                     })
//                 };
//             }
//         },
//         minimumInputLength: 2
//     });
//  });
// });

