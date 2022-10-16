window.onload = function () {
    let page_elements = document.getElementsByClassName("page-link");
    Array.from(page_elements).forEach(function (element) {
        element.addEventListener('click', function () {
            document.getElementById('page').value = this.dataset.page;  // 페이지 링크의 data-page 속성값을 가져와서 폼에 입력.
            document.getElementById('searchForm').submit();
        });
    });
};