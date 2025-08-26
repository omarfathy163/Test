from odoo import http, _
from odoo.http import request

class UmrahPortal(http.Controller):

    @http.route(['/my/umrah/groups'], type='http', auth='user', website=True)
    def my_groups(self, **kwargs):
        groups = request.env['umrah.group'].sudo().search([])
        return request.render('umrah_tourism.portal_my_groups', {'groups': groups})

    @http.route(['/my/umrah/group/new'], type='http', auth='user', website=True, methods=['GET','POST'])
    def new_group(self, **post):
        if request.httprequest.method == "POST":
            vals = {
                'name': post.get('name'),
                'code': post.get('code'),
                'state': 'new',
            }
            request.env['umrah.group'].sudo().create(vals)
            return request.redirect('/my/umrah/groups')
        return request.render('umrah_tourism.portal_group_form', {})

    @http.route(['/my/umrah/pilgrims'], type='http', auth='user', website=True)
    def my_pilgrims(self, **kwargs):
        pilgrims = request.env['umrah.pilgrim'].sudo().search([])
        return request.render('umrah_tourism.portal_my_pilgrims', {'pilgrims': pilgrims})
