// 예약 취소 버튼을 누르면 실행하는 함수
function run_reservation_cancel() {

    var idx = document.getElementById('cancel_btn').value

    alert("예매 취소하시겠습니까?")
    location.href = '/inquiry/reser_cancel/?idx=' + idx
}


