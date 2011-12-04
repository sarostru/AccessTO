package find.my.services;

import java.util.List;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class service_list_item_adapater extends BaseAdapter{

	private List<ListItem> items;
	private Context context ;
	
	public service_list_item_adapater(Context context, List<ListItem> items) {
        this.context = context;
        this.items = items;
    }
	
	@Override
	public int getCount() {
		return items.size();
	}

	@Override
	public Object getItem(int pos) {
		return items.get(pos);
	}

	@Override
	public long getItemId(int position) {
		return position;
	}

	@Override
	public View getView(int position, View convertView, ViewGroup viewGroup) {
		ListItem entry = items.get(position);
        if (convertView == null) {
            LayoutInflater inflater = (LayoutInflater) context
                    .getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.list_item, null);
        }
        TextView tvTitle = (TextView) convertView.findViewById(R.id.tvServiceTitle);
        tvTitle.setText(entry.getText());

        ImageView imgIcon = (ImageView) convertView.findViewById(R.id.imgServiceIcon);
        imgIcon.setImageResource(entry.getImage());

        return convertView;
	}


}
