package find.my.services;

import java.util.List;

import android.graphics.drawable.Drawable;
import android.os.Bundle;

import com.google.android.maps.GeoPoint;
import com.google.android.maps.MapActivity;
import com.google.android.maps.MapView;
import com.google.android.maps.Overlay;
import com.google.android.maps.OverlayItem;


public class ServicesMap extends MapActivity{

	private MapView mapView;
	@Override
	protected boolean isRouteDisplayed() {
		return false;
	}
	
	@Override
	public void onCreate(Bundle savedInstanceState) {
	    super.onCreate(savedInstanceState);
	    setContentView(R.layout.map_layout);
	    
	    mapView = (MapView) findViewById(R.id.mapview);
	    mapView.getController().setZoom(13);
	    
	    List<Overlay> mapOverlays = mapView.getOverlays();
	    Drawable drawable = this.getResources().getDrawable(R.drawable.accessibility);
	    MapOverlay itemizedoverlay = new MapOverlay(drawable, this);
	    
	    OverlayItem overlayitem1 = new OverlayItem(new GeoPoint(43760523,-79455903), "IRVING W CHAPLEY CC", "1.5 Km Away" );
	    OverlayItem overlayitem2 = new OverlayItem(new GeoPoint(43769773,-79524113), "JOHN BOOTH ARENA", "1.7 Km Away" );
	    OverlayItem overlayitem3 = new OverlayItem(new GeoPoint(43669258,-79553858), "JOHN G. ALTHOUSE CS", "1.7 Km Away" );
	    
	    itemizedoverlay.addOverlay(overlayitem1);
	    itemizedoverlay.addOverlay(overlayitem2);
	    itemizedoverlay.addOverlay(overlayitem3);
	    
	    mapOverlays.add(itemizedoverlay);
	    
	}
	
}