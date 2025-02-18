"""Test the Z-Wave JS button entities."""
from homeassistant.components.button.const import DOMAIN as BUTTON_DOMAIN, SERVICE_PRESS
from homeassistant.const import ATTR_ENTITY_ID


async def test_ping_entity(
    hass,
    client,
    climate_radio_thermostat_ct100_plus_different_endpoints,
    integration,
):
    """Test ping entity."""
    client.async_send_command.return_value = {"responded": True}

    # Test successful ping call
    await hass.services.async_call(
        BUTTON_DOMAIN,
        SERVICE_PRESS,
        {
            ATTR_ENTITY_ID: "button.z_wave_thermostat_ping",
        },
        blocking=True,
    )

    assert len(client.async_send_command.call_args_list) == 1
    args = client.async_send_command.call_args_list[0][0][0]
    assert args["command"] == "node.ping"
    assert (
        args["nodeId"]
        == climate_radio_thermostat_ct100_plus_different_endpoints.node_id
    )

    client.async_send_command.reset_mock()
