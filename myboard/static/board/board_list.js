function formCheck() {
    let searchType = document.getElementById('searchType');
    let searchWord = document.getElementById('searchWord');

    return (searchType && searchWord) ? true : false;
}

window.onload = function () {
    let page_elements = document.getElementsByClassName("page-link");
    Array.from(page_elements).forEach(function (element) {
        element.addEventListener('click', function () {
            document.getElementById('page').value = this.dataset.page;
            document.getElementById('searchForm').submit();
        });
    });
};