<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%
	String oneDay = request.getParameter("oneDay");
	out.println("oneDay: "+oneDay);
	
	Cookie reqCookies[] = request.getCookies();
	out.println("<p>my Cookies</p>");	
	if(reqCookies!=null) {
		for(Cookie c : reqCookies) {
			out.println(c.getValue());
		}
	}
	%>
	<script src="js/jquery-3.6.0.min.js"></script>
	<script>
	$.ajax({
		url: "cookiePopup.jsp",
		type: "get",
		data: {"oneDay": "ajaxOneDay"}
	})
	</script>
	<% out.println("oneDay: "+oneDay); %>
</body>
</html>