# -*- coding: utf-8 -*-
"""Test Layer for customer.diazo.mlsnica_com."""

# zope imports
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
    applyProfile,
)
from plone.testing import (
    Layer,
    z2,
)
from zope.configuration import xmlconfig


class CustomerDiazoMlsnicaComLayer(PloneSandboxLayer):
    """Custom Test Layer for customer.diazo.mlsnica_com."""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import customer.diazo.mlsnica_com
        xmlconfig.file(
            'configure.zcml',
            customer.diazo.mlsnica_com,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'customer.diazo.mlsnica_com:default')


CUSTOMER_DIAZO_MLSNICA_COM_FIXTURE = CustomerDiazoMlsnicaComLayer()


CUSTOMER_DIAZO_MLSNICA_COM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CUSTOMER_DIAZO_MLSNICA_COM_FIXTURE,),
    name='CustomerDiazoMlsnicaComLayer:IntegrationTesting'
)


CUSTOMER_DIAZO_MLSNICA_COM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CUSTOMER_DIAZO_MLSNICA_COM_FIXTURE,),
    name='CustomerDiazoMlsnicaComLayer:FunctionalTesting'
)


CUSTOMER_DIAZO_MLSNICA_COM_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CUSTOMER_DIAZO_MLSNICA_COM_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CustomerDiazoMlsnicaComLayer:AcceptanceTesting'
)


ROBOT_TESTING = Layer(name='customer.diazo.mlsnica_com:Robot')
