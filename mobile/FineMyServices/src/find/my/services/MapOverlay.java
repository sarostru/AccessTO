package find.my.services;

import java.util.ArrayList;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.widget.Toast;

import com.google.android.maps.OverlayItem;

public class MapOverlay extends com.google.android.maps.ItemizedOverlay {

	private ArrayList<OverlayItem> mOverlays = new ArrayList<OverlayItem>();
	private Context mContext;

	public MapOverlay(Drawable defaultMarker, Context context) {
		super(boundCenterBottom(defaultMarker));
		mContext = context;
	}

	public MapOverlay(Drawable defaultMarker) {
		super(boundCenterBottom(defaultMarker));
	}

	@Override
	protected OverlayItem createItem(int i) {
		return mOverlays.get(i);
	}

	@Override
	public int size() {
		return mOverlays.size();
	}

	@Override
	protected boolean onTap(int index) {
	  OverlayItem item = mOverlays.get(index);
	  AlertDialog.Builder dialog = new AlertDialog.Builder(mContext);
	  dialog.setTitle(item.getTitle());
	  dialog.setMessage(item.getSnippet())
	  .setCancelable(false)
	  .setPositiveButton("Show Details", new DialogInterface.OnClickListener() {
								  public void onClick(DialogInterface dialog, int id) {
									  //Toast.makeText(mContext, "Showing Details", Toast.LENGTH_LONG).show();
									  dialog.cancel();
									  Intent intent = new Intent(mContext, FacilityDetails.class);
									  mContext.startActivity(intent);
								  }
							  }
	  )
	  .setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
								  public void onClick(DialogInterface dialog, int id) {
									  dialog.cancel();
								  }
	  						  }
	  );
	  dialog.setIcon(R.drawable.accessibility);
	  dialog.show();
	  return true;
	}

	public void addOverlay(OverlayItem overlay) {
		mOverlays.add(overlay);
		populate();
	}
}
