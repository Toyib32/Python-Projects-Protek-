/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bangunruang;

/**
 *
 * @author ASUS
 */
public class Bola {
        //atribut 
    public int r;
    
    //method 
    public void hitungVolumeBola(){
        double vol = (4 / 3) * 3.14 * Math.pow(r, 3);
        System.out.println("volume bola adalah : " + vol);
    }
    
    public void hitungSelimutBola(){
        double selimut = 4 * 3.14 * r * r; 
        System.out.println("Luas selimut bola adalah : " + selimut);
    }
}
