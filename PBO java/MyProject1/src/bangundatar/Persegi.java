/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bangundatar;

/**
 *
 * @author ASUS
 */
public class Persegi {
    //atribut 
    public String namaPersegi;
    public int sisi;
    
    //method 
    public void hitungLuasPersegi(){
        int luas = sisi * sisi;
        System.out.println("Luas Persegi " + namaPersegi + " adalah ; " + luas);
    }
    
    public void hitungKelilingPersegi(){
        int keliling = 4 * sisi;
        System.out.println("Keliling persegi " + namaPersegi + " adalah ;" + keliling);
    }
}
