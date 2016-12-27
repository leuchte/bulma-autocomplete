import sublime_plugin
import sublime

bulma_classes = ["block","box","button","card","card-content","card-footer","card-footer-item","card-header","card-header-icon","card-header-title","card-image","column","columns","container","content","control","control-label","delete","fa","footer","has-addons","has-addons-centered","has-addons-fullwidth","has-addons-right","has-icon","has-icon-right","has-shadow","has-text-centered","has-text-left","has-text-right","heading","help","hero","hero-body","hero-buttons","hero-foot","hero-video","highlight","icon","image","input","is-1","is-1-desktop","is-1-mobile","is-1-tablet","is-1-widescreen","is-10","is-10-desktop","is-10-mobile","is-10-tablet","is-10-widescreen","is-11","is-11-desktop","is-11-mobile","is-11-tablet","is-11-widescreen","is-12","is-12-desktop","is-12-mobile","is-12-tablet","is-12-widescreen","is-128x128","is-16by9","is-16x16","is-1by1","is-2","is-2-desktop","is-2-mobile","is-2-tablet","is-2-widescreen","is-24x24","is-2by1","is-3","is-3-desktop","is-3-mobile","is-3-tablet","is-3-widescreen","is-32x32","is-3by2","is-4","is-4-desktop","is-4-mobile","is-4-tablet","is-4-widescreen","is-48x48","is-4by3","is-5","is-5-desktop","is-5-mobile","is-5-tablet","is-5-widescreen","is-6","is-6-desktop","is-6-mobile","is-6-tablet","is-6-widescreen","is-64x64","is-7","is-7-desktop","is-7-mobile","is-7-tablet","is-7-widescreen","is-8","is-8-desktop","is-8-mobile","is-8-tablet","is-8-widescreen","is-9","is-9-desktop","is-9-mobile","is-9-tablet","is-9-widescreen","is-96x96","is-active","is-ancestor","is-black","is-block","is-block-desktop","is-block-desktop-only","is-block-mobile","is-block-tablet","is-block-tablet-only","is-block-touch","is-block-widescreen","is-bold","is-bordered","is-boxed","is-brand","is-center","is-centered","is-child","is-clearfix","is-clipped","is-danger","is-dark","is-desktop","is-disabled","is-expanded","is-flex","is-flex-desktop","is-flex-desktop-only","is-flex-mobile","is-flex-tablet","is-flex-tablet-only","is-flex-touch","is-flex-widescreen","is-flexible","is-fluid","is-full","is-full-desktop","is-full-mobile","is-full-tablet","is-full-widescreen","is-fullheight","is-fullwidth","is-gapless","is-grid","is-grouped","is-grouped-centered","is-grouped-right","is-half","is-half-desktop","is-half-mobile","is-half-tablet","is-half-widescreen","is-hidden","is-hidden-desktop","is-hidden-desktop-only","is-hidden-mobile","is-hidden-tablet","is-hidden-tablet-only","is-hidden-touch","is-hidden-widescreen","is-horizontal","is-icon","is-info","is-inline","is-inline-block","is-inline-block-desktop","is-inline-block-desktop-only","is-inline-block-mobile","is-inline-block-tablet","is-inline-block-tablet-only","is-inline-block-touch","is-inline-block-widescreen","is-inline-desktop","is-inline-desktop-only","is-inline-flex","is-inline-flex-desktop","is-inline-flex-desktop-only","is-inline-flex-mobile","is-inline-flex-tablet","is-inline-flex-tablet-only","is-inline-flex-touch","is-inline-flex-widescreen","is-inline-mobile","is-inline-tablet","is-inline-tablet-only","is-inline-touch","is-inline-widescreen","is-inverted","is-large","is-left","is-light","is-link","is-loading","is-marginless","is-medium","is-mobile","is-multiline","is-narrow","is-narrow-desktop","is-narrow-mobile","is-narrow-tablet","is-narrow-widescreen","is-normal","is-offset-1","is-offset-1-desktop","is-offset-1-mobile","is-offset-1-tablet","is-offset-1-widescreen","is-offset-10","is-offset-10-desktop","is-offset-10-mobile","is-offset-10-tablet","is-offset-10-widescreen","is-offset-11","is-offset-11-desktop","is-offset-11-mobile","is-offset-11-tablet","is-offset-11-widescreen","is-offset-12","is-offset-12-desktop","is-offset-12-mobile","is-offset-12-tablet","is-offset-12-widescreen","is-offset-2","is-offset-2-desktop","is-offset-2-mobile","is-offset-2-tablet","is-offset-2-widescreen","is-offset-3","is-offset-3-desktop","is-offset-3-mobile","is-offset-3-tablet","is-offset-3-widescreen","is-offset-4","is-offset-4-desktop","is-offset-4-mobile","is-offset-4-tablet","is-offset-4-widescreen","is-offset-5","is-offset-5-desktop","is-offset-5-mobile","is-offset-5-tablet","is-offset-5-widescreen","is-offset-6","is-offset-6-desktop","is-offset-6-mobile","is-offset-6-tablet","is-offset-6-widescreen","is-offset-7","is-offset-7-desktop","is-offset-7-mobile","is-offset-7-tablet","is-offset-7-widescreen","is-offset-8","is-offset-8-desktop","is-offset-8-mobile","is-offset-8-tablet","is-offset-8-widescreen","is-offset-9","is-offset-9-desktop","is-offset-9-mobile","is-offset-9-tablet","is-offset-9-widescreen","is-offset-half","is-offset-half-desktop","is-offset-half-mobile","is-offset-half-tablet","is-offset-half-widescreen","is-offset-one-quarter","is-offset-one-quarter-desktop","is-offset-one-quarter-mobile","is-offset-one-quarter-tablet","is-offset-one-quarter-widescreen","is-offset-one-third","is-offset-one-third-desktop","is-offset-one-third-mobile","is-offset-one-third-tablet","is-offset-one-third-widescreen","is-offset-three-quarters","is-offset-three-quarters-desktop","is-offset-three-quarters-mobile","is-offset-three-quarters-tablet","is-offset-three-quarters-widescreen","is-offset-two-thirds","is-offset-two-thirds-desktop","is-offset-two-thirds-mobile","is-offset-two-thirds-tablet","is-offset-two-thirds-widescreen","is-one-quarter","is-one-quarter-desktop","is-one-quarter-mobile","is-one-quarter-tablet","is-one-quarter-widescreen","is-one-third","is-one-third-desktop","is-one-third-mobile","is-one-third-tablet","is-one-third-widescreen","is-outlined","is-overlay","is-paddingless","is-parent","is-primary","is-pulled-left","is-pulled-right","is-right","is-rounded","is-small","is-square","is-striped","is-success","is-tab","is-three-quarters","is-three-quarters-desktop","is-three-quarters-mobile","is-three-quarters-tablet","is-three-quarters-widescreen","is-toggle","is-transparent","is-two-thirds","is-two-thirds-desktop","is-two-thirds-mobile","is-two-thirds-tablet","is-two-thirds-widescreen","is-unselectable","is-vcentered","is-vertical","is-warning","is-white","label","level","level-item","level-left","level-right","loader","media","media-content","media-left","media-number","media-right","menu-label","menu-list","menu-nav","message","message-body","message-header","modal","modal-background","modal-card","modal-card-body","modal-card-foot","modal-card-head","modal-card-title","modal-close","nav","nav-center","nav-item","nav-left","nav-menu","nav-right","nav-toggle","notification","number","pagination","panel","panel-block","panel-heading","panel-icon","panel-list","panel-tabs","progress","radio","section","select","subtitle","table","tabs","tag","textarea","tile","title"]

class BulmaCompletions(sublime_plugin.EventListener):
    """
    Provide tag completions for Bulma elements and data-uk attributes
    """
    def __init__(self):

        self.class_completions = [("%s \tBulma CSS Framework Class" % s, s) for s in bulma_classes]

    def on_query_completions(self, view, prefix, locations):

        if view.match_selector(locations[0], "text.html string.quoted"):

            # Cursor is inside a quoted attribute
            # Now check if we are inside the class attribute

            # max search size
            LIMIT  = 250

            # place search cursor one word back
            cursor = locations[0] - len(prefix) - 1

            # dont start with negative value
            start  = max(0, cursor - LIMIT - len(prefix))

            # get part of buffer
            line   = view.substr(sublime.Region(start, cursor))

            # split attributes
            parts  = line.split('=')

            # is the last typed attribute a class attribute?
            if len(parts) > 1 and parts[-2].strip().endswith("class"):
                return self.class_completions
            else:
                return []
        elif view.match_selector(locations[0], "text.html meta.tag - text.html punctuation.definition.tag.begin"):

            # Cursor is in a tag, but not inside an attribute, i.e. <div {here}>
            # This one is easy, just return completions for the data-uk-* attributes
            return self.data_completions

        else:

            return []
