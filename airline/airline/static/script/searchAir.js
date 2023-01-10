// 편도일때 ow_selectflight로 보내는 함수
function send_to_ow() {
    var frm = document.forms['frm'];

    depart = frm['depart'].value;
    arri = frm['arri'].value;

    if($('input[type=radio][id=select4]').is(':checked')) {
        document.frm.action = "/reservation/ow_selectflight/";
    }
}

// form을 submit할 때 거치는 함수
function prec(){
    
    var depart = document.frm.depart.value;
    var arri = document.frm.arri.value;
    var goDate = document.frm.goDate.value;
    var user_id = document.frm.user_id.value;

    if(depart == "") {
        alert("출발지를 선택해주세요");
        return false
    } else if(arri == "") {
        alert("도착지를 선택해주세요");
        return false
    } else if(goDate == "") {
        alert("가는날을 선택해주세요");
        return false
    }

    send_to_ow();

    //로그인 했는지 체크 없으면 로그인 페이지로
    if(user_id == "") {
        alert("로그인을 해주세요");
        location.href = 'login/loginForm';
        return false
    }

    return true
    

}

// 출발지, 도착지 눌렀을 때 나오는 팝업
function choice_de(){
    alert('함수...')

    // var con = document.getElementsByClassName("popup");
    // if(con.style.display == 'none'){
    //     con.style.display = 'block';
    // } else {
    //     con.style.display = 'none';
    // }

    $('.popup').css("display", "block");

}

// 편도 선택시 오는날 선택부분이 사라지는 함수
function select_way() {

    if($('input[type=radio][id=select4]').is(':checked')) {

        alert('오는날이 사라져야 한다.')
        $('.arri').hide();
    } else {
        $('.arri').show();
    }

}


