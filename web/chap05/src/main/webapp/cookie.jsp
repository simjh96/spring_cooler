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
	response.addCookie(new Cookie("visited","true"));

	Cookie reqCookies[] = request.getCookies();
	out.println("<p>visited?</p>");
	
	if(reqCookies!=null) {
		for(Cookie c : reqCookies) {
			out.println(c.getValue());
		}
	} else {
		System.out.print("no cookie found at first");
		%>
		<script>location.reload()</script>
		<% 
	}
	%>
</body>
</html>