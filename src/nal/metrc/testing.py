# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import nal.metrc


class NalMetrcLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=nal.metrc)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'nal.metrc:default')


NAL_METRC_FIXTURE = NalMetrcLayer()


NAL_METRC_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NAL_METRC_FIXTURE,),
    name='NalMetrcLayer:IntegrationTesting',
)


NAL_METRC_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NAL_METRC_FIXTURE,),
    name='NalMetrcLayer:FunctionalTesting',
)


NAL_METRC_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NAL_METRC_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='NalMetrcLayer:AcceptanceTesting',
)
