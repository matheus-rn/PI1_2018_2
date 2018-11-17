function openNav() {
    document.getElementById("mySidenav").style.width = "30%";
    document.getElementById("main").style.marginLeft = "30%";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}


function update_clock() {
    var today = new Date
    var hours = today.getHours()
    var minutes = today.getMinutes()
    var seconds = today.getSeconds()
    clock = document.getElementById('clock')
    clock.value = hours + ":" + minutes + ":" + seconds
    setTimeout('update_clock()', 1000)
}