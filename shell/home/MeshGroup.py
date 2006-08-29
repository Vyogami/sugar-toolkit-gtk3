import random

import goocanvas

from sugar.canvas.IconItem import IconItem
from sugar.canvas.IconItem import IconColor
from sugar import conf

import Theme

class ActivityItem(IconItem):
	def __init__(self, activity):
		registry = conf.get_activity_registry()
		info = registry.get_activity(activity.get_type())
		icon_name = info.get_icon()

		IconItem.__init__(self, icon_name=icon_name,
						  color=activity.get_color(), size=48)

		self._activity = activity

	def get_service(self):
		return self._activity.get_service()

class MeshGroup(goocanvas.Group):
	def __init__(self, data_model):
		goocanvas.Group.__init__(self)
		self._theme = Theme.get_instance()
		self._theme.connect("theme-changed", self.__theme_changed_cb)

		color = self._theme.get_home_mesh_color()
		self._mesh_rect = goocanvas.Rect(width=1200, height=900,
										 fill_color=color)
		self.add_child(self._mesh_rect)

		for activity in data_model:
			self.add_activity(activity)

		data_model.connect('activity-added', self.__activity_added_cb)

	def __theme_changed_cb(self, theme):
		pass

	def add_activity(self, activity):
		item = ActivityItem(activity)
		item.set_property('x', random.random() * 1100)
		item.set_property('y', random.random() * 800)
		self.add_child(item)

	def __activity_added_cb(self, data_model, activity):
		self.add_activity(activity)	

#	def __activity_button_press_cb(self, view, target, event, service):
#		self._shell.join_activity(service)
#
#	def __item_view_created_cb(self, view, item_view, item):
#		if isinstance(item, ActivityItem):
#			item_view.connect("button_press_event",
#							  self.__activity_button_press_cb,
#							  item.get_service())
