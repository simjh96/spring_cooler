<%@page import="java.util.ArrayList"%>
<%@page import="com.simjh96.chap05.MemberDto"%>
<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	List<MemberDto> memberList = new ArrayList<>();
	memberList.add(new MemberDto("토르","thor"));
	memberList.add(new MemberDto("토니스타크","ironman"));
	pageContext.setAttribute("avengers", memberList);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	
</body>
</html>