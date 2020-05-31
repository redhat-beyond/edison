var right_edge

function ajaxCall(url, data, method, successCallback, errorCallback) {
	$.ajax({
		method: method,
		dataType: "json",
		url: url,
		data: data,
		success: successCallback,
		error: errorCallback
	});
}

function signupBtn() {
	ajaxCall(
		'signup',
		{
			'username': $("#main_form_email").val(),
			'password': $("#main_form_password").val()
		}, "POST", 
		function(data) {
			window.location.replace("/");
		}, function(data) {
			console.log(data);
			$("#error_message").text(data).delay(5000).fadeOut(400);
		}
	);
}

function signinBtn() {
	ajaxCall(
		'login',
		{
			'username': $("#main_form_email").val(),
			'password': $("#main_form_password").val()
		}, "POST", 
		function(data) {
			window.location.replace("/");
		}, function(data) {
			console.log(data);
			$("#error_message").text(data).delay(5000).fadeOut(400);
		}
	);
}


$(function() {
	$("main_block_btn").onclick = signinBtn;
    
	$("#btn_signup").click(function() {
		$("main_block_btn").onclick = signupBtn;
		$("#btn_forgot_password").fadeOut(0);
		$("#hide_div_back").css("display", "block");
		$("#sub_text_div").css("display", "none");
		$("#right_login").css("display", "block");
		$("#main_block_btn").text("SIGN UP");
		$("#main_block_title").text("sign up");
		right_edge = $("#right_edge")
		$("#right_edge").remove();
		$("#main_block").animate({
            left: "-150px",
			},
			250, 'linear', function() {
			});
	});
	
    $("#btn_right_login").click(function() {
		$("main_block_btn").onclick = signinBtn;
		$("#btn_forgot_password").fadeIn(0);
		$("#sub_text_div").css("display", "block");
		$("#login_screen").append(right_edge);
		$("#main_block").animate({
            left: "0px",
			},
			250, 'linear', function() {
			});
		$("#right_login").css("display", "none");
		$("#main_block_btn").text("LOG IN");
		$("#main_block_title").text("log in");
	});
});
