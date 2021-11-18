import json

def data_create_segment(segment_name):
    data = {
        "name": segment_name,
        "pass_condition": 1,
        "relations": [{"object_type": "remarketing_player", "params": {"type": "positive", "left": 365, "right": 0}}],
        "logicType": "or"
    }
    dumpdata = json.dumps(data)
    return dumpdata

def data_delete_segment(segment_id):
    data = [
        {
            "source_id": segment_id,
            "source_type": "segment"
        }
    ]
    dumpdata = json.dumps(data)
    return dumpdata

def data_create_company(company_name, primary_id, img_id):
    data = {"name": company_name,
            "objective": "traffic",
            "budget_limit_day": "100",
            "budget_limit": "100",
            "package_id": 961,
            "banners": [
                {
                    "urls": {"primary": {"id": primary_id}},
                    "content": {"image_240x400": {"id": img_id}}
                }
            ]
            }
    dumpdata = json.dumps(data)
    return dumpdata

def data_delete_company(company_id):
    data = [
        {
            "id": company_id, "status": "deleted"
        }
    ]
    dumpdata = json.dumps(data)
    return dumpdata

def data_check_company(user_id):
    data = {'fields': f'&_status__in=active\
    &_user_id__in={user_id}&'
            }
    dumpdata = json.dumps(data)
    return dumpdata