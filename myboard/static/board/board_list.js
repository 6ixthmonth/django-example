window.onload = function () {
    // 페이지 링크에 클릭 이벤트 적용.
    let page_elements = document.getElementsByClassName("page-link");
    Array.from(page_elements).forEach(function (element) {
        element.addEventListener('click', function () {
            document.getElementById('page').value = this.dataset.page;  // 페이지 링크의 data-page 속성값을 가져와서 폼에 입력.
            document.getElementById('form_search').submit();
        });
    });

    // 검색 버튼에 클릭 이벤트 적용.
    let btn_search = document.getElementById("btn_search");
    btn_search.addEventListener('click', function () {
        document.getElementById('page').value = 1;  // 페이지 번호를 1로 설정.
        document.getElementById('form_search').submit();
    });
};