package controllers;

import play.mvc.Controller;
import play.mvc.Result;

public class HomeAction extends Controller{
	public static Result home(){
		return ok(
				views.html.home.render("Test for home")
		);
	}
	
	
}
