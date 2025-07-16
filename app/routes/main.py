from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/blocks/<int:field_id>')
@login_required
def blocks_gallery(field_id):
    blocks = [
        {
            'name': 'B1',
            'versions': {
                'Orthomap': {'current': '1.2', 'all_versions': ['1.0', '1.1', '1.2']},
                'Field Boundary': {'current': '2.0', 'all_versions': ['1.0', '2.0']},
                'TVWS Location': {'current': '1.1', 'all_versions': ['1.0', '1.1']},
                'Bin Location': {'current': '3.4', 'all_versions': ['3.0', '3.1', '3.4']},
                'Waypoints': {'current': '2.5', 'all_versions': ['2.0', '2.5']},
            },
            'info': {
                'created_by': 'gasguy@map.com',
                'hectarage': 8.5,
                'planting_density': 148,
                'fertilizer_type': 'NPK Green',
                'dosage': 2.5,
                'palm_count': 1250,
                'last_updated': '2025-07-16',
                'note': 'Final layout for drone spraying'
            }
        },

         {
            'name': 'B2',
            'versions': {
                'Orthomap': {'current': '1.2', 'all_versions': ['1.0', '1.1', '1.2']},
                'Field Boundary': {'current': '2.0', 'all_versions': ['1.0', '2.0']},
                'TVWS Location': {'current': '1.1', 'all_versions': ['1.0', '1.1']},
                'Bin Location': {'current': '3.4', 'all_versions': ['3.0', '3.1', '3.4']},
                'Waypoints': {'current': '2.5', 'all_versions': ['2.0', '2.5']},
            },
            'info': {
                'created_by': 'gasguy@map.com',
                'hectarage': 8.5,
                'planting_density': 148,
                'fertilizer_type': 'NPK Green',
                'dosage': 2.5,
                'palm_count': 1250,
                'last_updated': '2025-07-16',
                'note': 'Final layout for drone spraying'
            }
        },

         {
            'name': 'B3',
            'versions': {
                'Orthomap': {'current': '1.2', 'all_versions': ['1.0', '1.1', '1.2']},
                'Field Boundary': {'current': '2.0', 'all_versions': ['1.0', '2.0']},
                'TVWS Location': {'current': '1.1', 'all_versions': ['1.0', '1.1']},
                'Bin Location': {'current': '3.4', 'all_versions': ['3.0', '3.1', '3.4']},
                'Waypoints': {'current': '2.5', 'all_versions': ['2.0', '2.5']},
            },
            'info': {
                'created_by': 'gasguy@map.com',
                'hectarage': 8.5,
                'planting_density': 148,
                'fertilizer_type': 'NPK Green',
                'dosage': 2.5,
                'palm_count': 1250,
                'last_updated': '2025-07-16',
                'note': 'Final layout for drone spraying'
            }
        },

         {
            'name': 'B4',
            'versions': {
                'Orthomap': {'current': '1.2', 'all_versions': ['1.0', '1.1', '1.2']},
                'Field Boundary': {'current': '2.0', 'all_versions': ['1.0', '2.0']},
                'TVWS Location': {'current': '1.1', 'all_versions': ['1.0', '1.1']},
                'Bin Location': {'current': '3.4', 'all_versions': ['3.0', '3.1', '3.4']},
                'Waypoints': {'current': '2.5', 'all_versions': ['2.0', '2.5']},
            },
            'info': {
                'created_by': 'gasguy@map.com',
                'hectarage': 8.5,
                'planting_density': 148,
                'fertilizer_type': 'NPK Green',
                'dosage': 2.5,
                'palm_count': 1250,
                'last_updated': '2025-07-16',
                'note': 'Final layout for drone spraying'
            }
        },

         {
            'name': 'B5',
            'versions': {
                'Orthomap': {'current': '1.2', 'all_versions': ['1.0', '1.1', '1.2']},
                'Field Boundary': {'current': '2.0', 'all_versions': ['1.0', '2.0']},
                'TVWS Location': {'current': '1.1', 'all_versions': ['1.0', '1.1']},
                'Bin Location': {'current': '3.4', 'all_versions': ['3.0', '3.1', '3.4']},
                'Waypoints': {'current': '2.5', 'all_versions': ['2.0', '2.5']},
            },
            'info': {
                'created_by': 'gasguy@map.com',
                'hectarage': 8.5,
                'planting_density': 148,
                'fertilizer_type': 'NPK Green',
                'dosage': 2.5,
                'palm_count': 1250,
                'last_updated': '2025-07-16',
                'note': 'Final layout for drone spraying'
            }
        },

         {
            'name': 'B6',
            'versions': {
                'Orthomap': {'current': '1.2', 'all_versions': ['1.0', '1.1', '1.2']},
                'Field Boundary': {'current': '2.0', 'all_versions': ['1.0', '2.0']},
                'TVWS Location': {'current': '1.1', 'all_versions': ['1.0', '1.1']},
                'Bin Location': {'current': '3.4', 'all_versions': ['3.0', '3.1', '3.4']},
                'Waypoints': {'current': '2.5', 'all_versions': ['2.0', '2.5']},
            },
            'info': {
                'created_by': 'gasguy@map.com',
                'hectarage': 8.5,
                'planting_density': 148,
                'fertilizer_type': 'NPK Green',
                'dosage': 2.5,
                'palm_count': 1250,
                'last_updated': '2025-07-16',
                'note': 'Final layout for drone spraying'
            }
        },
        # Add more blocks if needed
    ]

    # Simulate field-to-estate mapping for the back button
    field_to_estate_map = {
        101: 1,
        102: 1
    }
    back_estate_id = field_to_estate_map.get(field_id, 1)

    return render_template(
        'blocksGallery.html',
        blocks=blocks,
        current_user=current_user,
        back_estate_id=back_estate_id
    )



@main_bp.route('/estate-gallery')
@login_required
def estate_gallery():
    estates = [
        {'id': 1, 'name': 'Diamond Jubilee Estate', 'region': 'CER', 'field_count': 2},
        {'id': 2, 'name': 'East Estate', 'region': 'CWR', 'field_count': 2},
    ]
    return render_template('estateGallery.html', estates=estates, current_user=current_user)

@main_bp.route('/fields/<int:estate_id>')
@login_required
def fields(estate_id):
    # Dummy estate name - you can replace with DB lookup later
    estate_name = next((e['name'] for e in [
        {'id': 1, 'name': 'Diamond Jubilee Estate'},
        {'id': 2, 'name': 'East Estate'}
    ] if e['id'] == estate_id), "Unknown Estate")

    # Dummy fields data - replace with DB query later
    fields = [
        {
            'id': 101,
            'name': 'Field A',
            'hectarage': 12.5,
            'planting_density': 140,
            'fertilizer_type': 'NPK 15-15-15',
            'dosage_per_palm': 0.3,
            'block_count': 4
        },
        {
            'id': 102,
            'name': 'Field B',
            'hectarage': 8.0,
            'planting_density': 135,
            'fertilizer_type': 'Organic',
            'dosage_per_palm': 0.25,
            'block_count': 3
        },
    ]
    return render_template('fieldsGallery.html', estate_name=estate_name, fields=fields, current_user=current_user)

@main_bp.route('/blocks/<int:field_id>')
@login_required
def blocks(field_id):
    # TODO: implement real blocks logic here
    return f"Showing blocks for field ID: {field_id}"


