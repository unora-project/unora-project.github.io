document.addEventListener("DOMContentLoaded", function () {
    const tables = document.querySelectorAll("main table");
    tables.forEach((table) => {
        $(table).DataTable({
            autoWidth: false,
            searching: true,
            responsive: true,
            fixedHeader: {
                headerOffset: 115,
            },
            info: true,
            pageLength: 15,
            layout: {
                topEnd: {
                    search: {
                        placeholder: "Enter a search term.."
                    }
                },
                bottomEnd: {
                    paging: {
                        boundaryNumbers: false,
                        previousNext: false
                    }
                }
            },
            order: {
                name: 'LVL',
                dir: 'asc'
            },
            columnDefs: [
                { width: "10%", targets: 0 }
            ]
        });
    });
});
