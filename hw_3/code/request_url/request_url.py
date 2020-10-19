from urllib.parse import urljoin


class RequestUrl:
    base_url = 'https://target.my.com'

    def get_csrf_token_url(self):
        url = urljoin(self.base_url, '/csrf/')
        return url

    def get_create_segment_url(self):
        url = urljoin(
            self.base_url,
            'https://target.my.com/api/v2/remarketing/segments.json?'
            'fields=relations__object_type,relations__object_id,relations__params,relations_count,'
            'id,name,pass_condition,created,campaign_ids,users,flags'
        )
        return url

    def get_segments_url(self, segment_id):
        url = urljoin(self.base_url, f'api/v2/remarketing/segments/{segment_id}/relations.json')
        return url

    def get_delete_segment_url(self, segment_id):
        url = urljoin(self.base_url, f'api/v2/remarketing/segments/{segment_id}.json')
        return url

    def get_login_url(self):
        url = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        return url
