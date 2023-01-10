// 편도일때 ow_selectflight로 보내는 함수
function send_to_ow() {
    var frm = document.forms['frm'];

    depart = frm['depart'].value;
    arri = frm['arri'].value;

    if($('input[type=radio][id=select4]').is(':checked')) {
        document.frm.action = "/reservation/ow_selectflight/";
    }
}

// reservation.html submit 함수
// form을 submit할 때 거치는 함수
function reservation_submit(){
    
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
        location.href = '/login/loginForm/';
        return false
    }

    return true
    

}


// no_money_type(1, 2, 3)이렇게 주어진걸 split하는 함수
function valueDivide() {
    if (document.frm.re_type.value == "마일리지예매") {
        var get_value = document.frm.mileage.value;
    } else {
        
        var get_value = document.frm.amount.value;
    }

    var no = get_value.split('_')[0];
    var money = get_value.split('_')[1];
    var type = get_value.split('_')[2];


    $('#no').attr('value', no);
    $('#money').attr('value',  money);
    $('#type').attr('value',type);

}


// selectflight.html 제출할 때의 함수
function send_info(){
    valueDivide();   // no_money_운임타입 split

    // 항공운임 마일리지와 회원의 마일리지를 비교, 
    // 적으면 다시(valueDivide() 보다 밑에 있어야 한다.)
    var m_point = Number(document.frm.m_point.value);
    var money = Number(document.frm.money.value);
    var re_type = document.frm.re_type.value;

    if(re_type == "예매") {
        if($('input[type=radio][name=amount]').is(':checked')) {
            // true면 아무것도 안함
        } else {
            alert("가격을 보고 선택해주세요");
            return false;
        }
    } else if(re_type == "마일리지예매") {
        if($('input[type=radio][name=mileage]').is(':checked')) {
            // true면 아무것도 안함
        } else {
            alert("가격을 보고 선택해주세요");
            return false;
        }
    
        if(m_point < money) {
            alert("마일리지가 부족합니다. \n다시 선택해주세요")
            return false
        }
    }


}

// ow_selectflight.html, selectflight2.html() 제출시 함수
function submit_info() {

    valueDivide();   // no_money_운임타입 split
    
    // 항공운임 마일리지와 회원의 마일리지를 비교, 
    // 적으면 다시(valueDivide() 보다 밑에 있어야 한다.)
    var m_point = Number(document.frm.m_point.value);
    var money = Number(document.frm.money.value);
    var re_type = document.frm.re_type.value;
 console.log("asdfasdf");
    if(re_type == "예매") {

        if($('input[type=radio][name=amount]').is(':checked')) {
            // true면 아무것도 안함
        } else {
            alert("가격을 보고 선택해주세요");
            return false;
        }
    } else if(re_type == "마일리지예매") {
    
        if($('input[type=radio][name=mileage]').is(':checked')) {
            // true면 아무것도 안함
        } else if(m_point < money) {
            alert("마일리지가 부족합니다. \n다시 선택해주세요")
            return false
        }
    }
}


// passabger_info 검사 함수
function genderLoad() {
    var frm = document.frm;
    var m_gender = frm.m_gender.value;

    if(m_gender == '0') {
        $('#male').prop("checked", true);
    } else if(m_gender == '1') {
        $('#female').prop("checked", true);
    } else {
        alert('이상한 값이 들어와 있습니다.');
    }

}
window.onload = genderLoad;


// 탑승객 정보 확인 버튼
function check_info() {
    document.frm.check1.value = 1;
}



// 약관등의 확인을 체크하는 함수
function check_agree() {
    var info_collect = document.frm.info_collect;
    var rule_agree = document.frm.rule_agree;
    var danger_agree = document.frm.danger_agree;

    if(info_collect.checked == false) {
        alert('개인정보 확인이 필요합니다');
        
    } else if(rule_agree.checked == false) {
        alert('운송약관 등의 규정 확인이 필요합니다.');
        
    } else if(danger_agree.checked == false) {
        alert('위험품 규정 확인이 필요합니다.');
    
    } else {
        $('#info_collect').attr('value', 1);
        $('#rule_agree').attr('value', 1);
        $('#danger_agree').attr('value', 1);
        document.frm.check2.value = 1;
    }
}


// transaction.html 제출할때 거치는 함수
function submit_trac() {
    var check1 = document.frm.check1.value;
    var check2 = document.frm.check2.value;

    if (check1 != 1) {
        alert("탑승객 정보 확인을 눌러주세요");
        return false
    }
    if (check2 != 1) {
        alert("약관동의 확인을 눌러주세요");
        return false
    }
}


// 편도일 때 오는 날을 숨기고 아닐 때 보여주는 함수
function show_way() {
    if($('input[type=radio][name=method]:checked').val() == '0') {
        document.getElementById("card_num_form").style.display = "block";
        document.getElementById("bank_account").style.display = "none";

    } else if ($('input[type=radio][name=method]:checked').val() == '1') {
        document.getElementById("card_num_form").style.display = "none";
        document.getElementById("bank_account").style.display = "block";
    } 
}


// paymentpage.html들에서 결제완료 alert창
function alert_pay() {
    alert("결제완료했습니다.")
}


