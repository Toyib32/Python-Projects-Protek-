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
public class Kerucut {
    //atribut 
    public int r;
    public int t;
    public int s; 
    
    //method 
    public void hitungVolumeKerucut(){
        double vol = ((3.14 * r * t) * t) / 3;
        System.out.println("volume kerucut adalah : " + vol);
    }
    
    public void hitungLuasSelimutKerucut(){
        double selimut = 3.14 * r * (r + s);
        System.out.println("luas selimut kerucut adalah : " + selimut);
    }
}
