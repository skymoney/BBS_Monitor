package models;

import java.util.*;

import javax.persistence.Entity;
import javax.persistence.Id;

import play.data.validation.Constraints.Required;
import play.db.ebean.Model;

@Entity
public class Task extends Model{
	
	@Id
	public Long id;
	
	@Required
	public String label;
	
	public static List<Task> all(){
		return new ArrayList<Task>();
	}
	
	public static void create(Task task){
		
	}
	
	public static void delete(Long id){
		
	}
}
