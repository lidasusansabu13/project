function transfer(){	
	var tablink;
	chrome.tabs.getSelected(null,function(tab) {
	   	tablink = tab.url;
		$("#p1").text("The URL being tested is - "+tablink);

		var xhr=new XMLHttpRequest();
		console.log(tablink)
		params ="127.0.0.1:8000/backend/check/?url="+tablink;
		alert(params);//comment1
		var markup = "url="+tablink+"&html="+document.documentElement.innerHTML;
		xhr.open(params,false);
                
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhr.send(markup);
		console.log(xhr);
		alert(xhr.responseText);//c2
		$("#div1").text(xhr.responseText);
		return xhr.responseText;
	});
}

$(document).ready(function(){
    $("button").click(function(){	
		var val = transfer();
    });
});

chrome.tabs.getSelected(null,function(tab) {
   	var tablink = tab.url;
	$("#p1").text("The URL being tested is - "+tablink);
});
