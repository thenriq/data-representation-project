host = window.location.origin
function GetMovie(){
    $.ajax({
        "url" : host + "/demo_request",
        "method": "GET",
        "data": "",
        "dataType" : "HTML",
        "success" : function (result) {
            console.log(result);
        },
        "error": function (xhr, status, error) {
            console.log("error: " + status + " msg:" + error); 
        }
    });
}

function NewMovie(){
    $.ajax({
        "url" : host + "/demo_request",
        "method": "POST",
        "data": "",
        "dataType" : "HTML",
        "success" : function (result) {
            console.log(result);
        },
        "error": function (xhr, status, error) {
            console.log("error: " + status + " msg:" + error); 
        }
    });
}

function EditMovie(){
    $.ajax({
        "url" : host + "/demo_request",
        "method": "PUT",
        "data": "",
        "dataType" : "HTML",
        "success" : function (result) {
            console.log(result);
        },
        "error": function (xhr, status, error) {
            console.log("error: " + status + " msg:" + error); 
        }
    });
}

function DeleteMovie(){
    $.ajax({
        "url" : host + "/demo_request",
        "method": "DELETE",
        "data": "",
        "dataType" : "HTML",
        "success" : function (result) {
            console.log(result);
        },
        "error": function (xhr, status, error) {
            console.log("error: " + status + " msg:" + error); 
        }
    });
}


$(document).click(function(){
    $("#BtnSearchMovie").click(function(){
        $("#searchform").modal();
    });

});

$(document).click(function(){
    $("#BtnLogin").click(function(){
        $("#loginModal").modal();
    });
});