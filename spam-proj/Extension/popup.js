function transfer(){	
	var tablink;
	chrome.tabs.getSelected(null,function(tab) {
	   	tablink = tab.url;
		$("#p1").text("The URL being tested is - "+tablink);

		var xhr=new XMLHttpRequest();
		console.log(tablink)
		params ="127.0.0.1:8000/backend/check/?url="+tab.url;
		//alert(params);//comment1
		var markup = "url="+tablink+"&html="+document.documentElement.innerHTML;
		xhr.open("GET","http://127.0.0.1:8000/backend/check/?url="+tablink,true);
                
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhr.send(markup);
		//console.log(xhr.responseText);
		xhr.onreadystatechange = function () {
			if (this.readyState == 4 && this.status == 200) {
					// displays response text in div with id  - 'message'
					//document.getElementById("message").innerHTML =this.responseText;
					//alerts response text
					alert("The website is "+this.responseText);
			}
		};


		$("#div1").text(JSON.stringify(xhr));
		return xhr.responseText;
	});
}

$(document).ready(function(){
    $("button").click(function(){	
		var val = transfer();
    });
});

/*chrome.tabs.getSelected(null,function(tab) {
   	var tablink = tab.url;
	$("#p1").text("The URL being tested is - "+tablink);
});*/
