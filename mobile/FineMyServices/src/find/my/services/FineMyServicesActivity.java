package find.my.services;

import java.util.ArrayList;
import java.util.List;

import android.app.ListActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;

public class FineMyServicesActivity extends ListActivity implements OnItemClickListener {
	/** Called when the activity is first created. */

	private List<ListItem> array_items;

	@Override
	public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        array_items = new ArrayList<ListItem>();

        array_items.add(new ListItem(R.drawable.childcare_big, "Childcare"));
        array_items.add(new ListItem(R.drawable.dental_big, "Dental"));
        array_items.add(new ListItem(R.drawable.recreation_big, "Recreation"));
        array_items.add(new ListItem(R.drawable.skating_big, "Skating"));
        array_items.add(new ListItem(R.drawable.swimming_big, "Swimming"));

        service_list_item_adapater arrayAdapter = new service_list_item_adapater(this, array_items);
        
        setListAdapter(arrayAdapter);
        ListView lv = getListView();
        lv.setTextFilterEnabled(true);
        
        lv.setOnItemClickListener(this);
	}
	
	@Override
	public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

		Intent intent = new Intent(FineMyServicesActivity.this,
				ServicesMap.class);
		intent.putExtra("Service", "ServiceNamDummy");
		FineMyServicesActivity.this.startActivity(intent);

	}

}