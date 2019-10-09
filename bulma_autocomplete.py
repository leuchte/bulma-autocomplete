import sublime_plugin
import sublime

# For Bulma v0.7.5
bulma_classes = ["block","box","breadcrumb","button","card","card-content","card-footer","card-footer-item","card-header","card-header-icon","card-header-title","card-image","column","columns","container","content","control","delete","dropdown","dropdown-content","dropdown-divider","dropdown-item","dropdown-menu","fa","field","field-body","field-label","file","file-cta","file-icon","file-input","file-label","file-name","footer","has-addons","has-addons-centered","has-addons-fullwidth","has-addons-right","has-arrow-separator","has-bullet-separator","has-dot-separator","has-dropdown","has-fixed-size","has-icon","has-icon-right","has-icons-left","has-icons-right","has-name","has-shadow","has-succeeds-separator","has-text-black","has-text-black-bis","has-text-black-ter","has-text-centered","has-text-centered-desktop","has-text-centered-desktop-only","has-text-centered-fullhd","has-text-centered-mobile","has-text-centered-tablet","has-text-centered-tablet-only","has-text-centered-touch","has-text-centered-widescreen","has-text-centered-widescreen-only","has-text-danger","has-text-dark","has-text-grey","has-text-grey-dark","has-text-grey-darker","has-text-grey-light","has-text-grey-lighter","has-text-info","has-text-justified","has-text-justified-desktop","has-text-justified-desktop-only","has-text-justified-fullhd","has-text-justified-mobile","has-text-justified-tablet","has-text-justified-tablet-only","has-text-justified-touch","has-text-justified-widescreen","has-text-justified-widescreen-only","has-text-left","has-text-left-desktop","has-text-left-desktop-only","has-text-left-fullhd","has-text-left-mobile","has-text-left-tablet","has-text-left-tablet-only","has-text-left-touch","has-text-left-widescreen","has-text-left-widescreen-only","has-text-light","has-text-link","has-text-primary","has-text-right","has-text-right-desktop","has-text-right-desktop-only","has-text-right-fullhd","has-text-right-mobile","has-text-right-tablet","has-text-right-tablet-only","has-text-right-touch","has-text-right-widescreen","has-text-right-widescreen-only","has-text-success","has-text-warning","has-text-weight-bold","has-text-weight-light","has-text-weight-normal","has-text-weight-semibold","has-text-white","has-text-white-bis","has-text-white-ter","heading","help","hero","hero-body","hero-buttons","hero-foot","hero-video","highlight","icon","image","input","is-0","is-1","is-1-desktop","is-1-fullhd","is-1-mobile","is-1-tablet","is-1-touch","is-1-widescreen","is-10","is-10-desktop","is-10-fullhd","is-10-mobile","is-10-tablet","is-10-touch","is-10-widescreen","is-11","is-11-desktop","is-11-fullhd","is-11-mobile","is-11-tablet","is-11-touch","is-11-widescreen","is-12","is-12-desktop","is-12-fullhd","is-12-mobile","is-12-tablet","is-12-touch","is-12-widescreen","is-128x128","is-16by9","is-16x16","is-1by1","is-2","is-2-desktop","is-2-fullhd","is-2-mobile","is-2-tablet","is-2-touch","is-2-widescreen","is-24x24","is-2by1","is-3","is-3-desktop","is-3-fullhd","is-3-mobile","is-3-tablet","is-3-touch","is-3-widescreen","is-32x32","is-3by2","is-4","is-4-desktop","is-4-fullhd","is-4-mobile","is-4-tablet","is-4-touch","is-4-widescreen","is-48x48","is-4by3","is-5","is-5-desktop","is-5-fullhd","is-5-mobile","is-5-tablet","is-5-touch","is-5-widescreen","is-6","is-6-desktop","is-6-fullhd","is-6-mobile","is-6-tablet","is-6-touch","is-6-widescreen","is-64x64","is-7","is-7-desktop","is-7-fullhd","is-7-mobile","is-7-tablet","is-7-touch","is-7-widescreen","is-8","is-8-desktop","is-8-fullhd","is-8-mobile","is-8-tablet","is-8-touch","is-8-widescreen","is-9","is-9-desktop","is-9-fullhd","is-9-mobile","is-9-tablet","is-9-touch","is-9-widescreen","is-96x96","is-active","is-ancestor","is-black","is-block","is-block-desktop","is-block-desktop-only","is-block-fullhd","is-block-mobile","is-block-tablet","is-block-tablet-only","is-block-touch","is-block-widescreen","is-block-widescreen-only","is-bold","is-bordered","is-boxed","is-capitalized","is-center","is-centered","is-child","is-clearfix","is-clipped","is-current","is-danger","is-dark","is-desktop","is-disabled","is-expanded","is-flex","is-flex-desktop","is-flex-desktop-only","is-flex-fullhd","is-flex-mobile","is-flex-tablet","is-flex-tablet-only","is-flex-touch","is-flex-widescreen","is-flex-widescreen-only","is-flexible","is-fluid","is-full","is-full-desktop","is-full-fullhd","is-full-mobile","is-full-tablet","is-full-touch","is-full-widescreen","is-fullhd","is-fullheight","is-fullwidth","is-gapless","is-grouped","is-grouped-centered","is-grouped-multiline","is-grouped-right","is-half","is-half-desktop","is-half-fullhd","is-half-mobile","is-half-tablet","is-half-touch","is-half-widescreen","is-halfheight","is-hidden","is-hidden-desktop","is-hidden-desktop-only","is-hidden-fullhd","is-hidden-mobile","is-hidden-tablet","is-hidden-tablet-only","is-hidden-touch","is-hidden-widescreen","is-hidden-widescreen-only","is-horizontal","is-hoverable","is-hovered","is-info","is-inline","is-inline-block","is-inline-block-desktop","is-inline-block-desktop-only","is-inline-block-fullhd","is-inline-block-mobile","is-inline-block-tablet","is-inline-block-tablet-only","is-inline-block-touch","is-inline-block-widescreen","is-inline-block-widescreen-only","is-inline-desktop","is-inline-desktop-only","is-inline-flex","is-inline-flex-desktop","is-inline-flex-desktop-only","is-inline-flex-fullhd","is-inline-flex-mobile","is-inline-flex-tablet","is-inline-flex-tablet-only","is-inline-flex-touch","is-inline-flex-widescreen","is-inline-flex-widescreen-only","is-inline-fullhd","is-inline-mobile","is-inline-tablet","is-inline-tablet-only","is-inline-touch","is-inline-widescreen","is-inline-widescreen-only","is-inverted","is-large","is-left","is-light","is-link","is-loading","is-lowercase","is-marginless","is-medium","is-mobile","is-multiline","is-narrow","is-narrow-desktop","is-narrow-fullhd","is-narrow-mobile","is-narrow-tablet","is-narrow-touch","is-narrow-widescreen","is-normal","is-offset-1","is-offset-1-desktop","is-offset-1-fullhd","is-offset-1-mobile","is-offset-1-tablet","is-offset-1-touch","is-offset-1-widescreen","is-offset-10","is-offset-10-desktop","is-offset-10-fullhd","is-offset-10-mobile","is-offset-10-tablet","is-offset-10-touch","is-offset-10-widescreen","is-offset-11","is-offset-11-desktop","is-offset-11-fullhd","is-offset-11-mobile","is-offset-11-tablet","is-offset-11-touch","is-offset-11-widescreen","is-offset-12","is-offset-12-desktop","is-offset-12-fullhd","is-offset-12-mobile","is-offset-12-tablet","is-offset-12-touch","is-offset-12-widescreen","is-offset-2","is-offset-2-desktop","is-offset-2-fullhd","is-offset-2-mobile","is-offset-2-tablet","is-offset-2-touch","is-offset-2-widescreen","is-offset-3","is-offset-3-desktop","is-offset-3-fullhd","is-offset-3-mobile","is-offset-3-tablet","is-offset-3-touch","is-offset-3-widescreen","is-offset-4","is-offset-4-desktop","is-offset-4-fullhd","is-offset-4-mobile","is-offset-4-tablet","is-offset-4-touch","is-offset-4-widescreen","is-offset-5","is-offset-5-desktop","is-offset-5-fullhd","is-offset-5-mobile","is-offset-5-tablet","is-offset-5-touch","is-offset-5-widescreen","is-offset-6","is-offset-6-desktop","is-offset-6-fullhd","is-offset-6-mobile","is-offset-6-tablet","is-offset-6-touch","is-offset-6-widescreen","is-offset-7","is-offset-7-desktop","is-offset-7-fullhd","is-offset-7-mobile","is-offset-7-tablet","is-offset-7-touch","is-offset-7-widescreen","is-offset-8","is-offset-8-desktop","is-offset-8-fullhd","is-offset-8-mobile","is-offset-8-tablet","is-offset-8-touch","is-offset-8-widescreen","is-offset-9","is-offset-9-desktop","is-offset-9-fullhd","is-offset-9-mobile","is-offset-9-tablet","is-offset-9-touch","is-offset-9-widescreen","is-offset-half","is-offset-half-desktop","is-offset-half-fullhd","is-offset-half-mobile","is-offset-half-tablet","is-offset-half-touch","is-offset-half-widescreen","is-offset-one-quarter","is-offset-one-quarter-desktop","is-offset-one-quarter-fullhd","is-offset-one-quarter-mobile","is-offset-one-quarter-tablet","is-offset-one-quarter-touch","is-offset-one-quarter-widescreen","is-offset-one-third","is-offset-one-third-desktop","is-offset-one-third-fullhd","is-offset-one-third-mobile","is-offset-one-third-tablet","is-offset-one-third-touch","is-offset-one-third-widescreen","is-offset-three-quarters","is-offset-three-quarters-desktop","is-offset-three-quarters-fullhd","is-offset-three-quarters-mobile","is-offset-three-quarters-tablet","is-offset-three-quarters-touch","is-offset-three-quarters-widescreen","is-offset-two-thirds","is-offset-two-thirds-desktop","is-offset-two-thirds-fullhd","is-offset-two-thirds-mobile","is-offset-two-thirds-tablet","is-offset-two-thirds-touch","is-offset-two-thirds-widescreen","is-one-quarter","is-one-quarter-desktop","is-one-quarter-fullhd","is-one-quarter-mobile","is-one-quarter-tablet","is-one-quarter-touch","is-one-quarter-widescreen","is-one-third","is-one-third-desktop","is-one-third-fullhd","is-one-third-mobile","is-one-third-tablet","is-one-third-touch","is-one-third-widescreen","is-outlined","is-overlay","is-paddingless","is-parent","is-primary","is-pulled-left","is-pulled-right","is-radiusless","is-right","is-selected","is-shadowless","is-size-1","is-size-1-desktop","is-size-1-fullhd","is-size-1-mobile","is-size-1-tablet","is-size-1-touch","is-size-1-widescreen","is-size-2","is-size-2-desktop","is-size-2-fullhd","is-size-2-mobile","is-size-2-tablet","is-size-2-touch","is-size-2-widescreen","is-size-3","is-size-3-desktop","is-size-3-fullhd","is-size-3-mobile","is-size-3-tablet","is-size-3-touch","is-size-3-widescreen","is-size-4","is-size-4-desktop","is-size-4-fullhd","is-size-4-mobile","is-size-4-tablet","is-size-4-touch","is-size-4-widescreen","is-size-5","is-size-5-desktop","is-size-5-fullhd","is-size-5-mobile","is-size-5-tablet","is-size-5-touch","is-size-5-widescreen","is-size-6","is-size-6-desktop","is-size-6-fullhd","is-size-6-mobile","is-size-6-tablet","is-size-6-touch","is-size-6-widescreen","is-size-7","is-size-7-desktop","is-size-7-fullhd","is-size-7-mobile","is-size-7-tablet","is-size-7-touch","is-size-7-widescreen","is-small","is-square","is-static","is-striped","is-success","is-tab","is-text","is-three-quarters","is-three-quarters-desktop","is-three-quarters-fullhd","is-three-quarters-mobile","is-three-quarters-tablet","is-three-quarters-touch","is-three-quarters-widescreen","is-toggle","is-transparent","is-two-thirds","is-two-thirds-desktop","is-two-thirds-fullhd","is-two-thirds-mobile","is-two-thirds-tablet","is-two-thirds-touch","is-two-thirds-widescreen","is-unselectable","is-up","is-uppercase","is-variable","is-vcentered","is-vertical","is-warning","is-white","is-widescreen","is-wrapped","label","level","level-item","level-left","level-right","loader","media","media-content","media-left","media-right","menu","menu-label","menu-list","message","message-body","message-header","modal","modal-background","modal-card","modal-card-body","modal-card-foot","modal-card-head","modal-card-title","modal-close","navbar","navbar-brand","navbar-burger","navbar-content","navbar-divider","navbar-dropdown","navbar-end","navbar-item","navbar-link","navbar-menu","navbar-start","navbar-tabs","notification","number","pagination","pagination-ellipsis","pagination-link","pagination-list","pagination-next","pagination-previous","panel","panel-block","panel-heading","panel-icon","panel-list","panel-tabs","progress","radio","section","select","subtitle","table","tabs","tag","tags","textarea","tile","title"]

class BulmaCompletions(sublime_plugin.EventListener):
    """
    Provide tag completions for Bulma elements and data-uk attributes
    """
    def __init__(self):

        self.class_completions = [("%s \tBulma CSS Class" % s, s) for s in bulma_classes]

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
