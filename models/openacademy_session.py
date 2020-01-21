from odoo import models, fields, api

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Open Academy Sessions'

    name = fields.Char(
        required=True,
    )
    start_date = fields.Date(
    )
    duration = fields.Float(
        digits=(6, 2),
        help='Duration in days',
    )
    seats = fields.Integer(
        string='Number of seats',
    )
    instructor_id = fields.Many2one(
        comodel_name='res.partner',
        string='Instructor',
        domain=[
                '|', 
                ('instructor', '=', True),
                ('category_id.name', 'ilike', "Teacher"),
            ]

    )
    course_id = fields.Many2one(
        comodel_name='openacademy.course',
        ondelete='cascade',
        string='Course',
        required=True,
    )
    attendee_ids = fields.Many2many(
        comodel_name='res.partner', 
        string="Attendees",
    )



    #_id Many2one 
    #_ids One2many o Many2many